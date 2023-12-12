import numpy

class DataPreprocessor:
    @staticmethod
    def split_list(attr, labels):
        total_samples = attr.shape[0]
        train_size = int(total_samples * 0.7)

        indices = numpy.random.permutation(total_samples)
        training_idx, test_idx = indices[:train_size], indices[train_size:]

        training_attr, test_attr = attr[training_idx, :], attr[test_idx, :]
        training_labels, test_labels = labels[training_idx, :], labels[test_idx, :]

        return training_attr, training_labels, test_attr, test_labels

    @staticmethod
    def normalize_data(attr_arr, labels):
        price_list = attr_arr[:, 0]
        range_price = (max(price_list) - min(price_list))

        attr_arr[:, 0] = attr_arr[:, 0] / range_price

        return attr_arr, labels
