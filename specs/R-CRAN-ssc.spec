%global __brp_check_rpaths %{nil}
%global packname  ssc
%global packver   2.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Semi-Supervised Classification Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-proxy 
Requires:         R-stats 
Requires:         R-CRAN-proxy 

%description
Provides a collection of self-labeled techniques for semi-supervised
classification. In semi-supervised classification, both labeled and
unlabeled data are used to train a classifier. This learning paradigm has
obtained promising results, specifically in the presence of a reduced set
of labeled examples. This package implements a collection of self-labeled
techniques to construct a classification model. This family of techniques
enlarges the original labeled set using the most confident predictions to
classify unlabeled data. The techniques implemented can be applied to
classification problems in several domains by the specification of a
supervised base classifier. At low ratios of labeled data, it can be shown
to perform better than classical supervised classifiers.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
