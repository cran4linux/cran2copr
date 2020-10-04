%global packname  CVThresh
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Level-Dependent Cross-Validation Thresholding

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-wavethresh >= 4.6.1
BuildRequires:    R-CRAN-EbayesThresh >= 1.3.2
Requires:         R-CRAN-wavethresh >= 4.6.1
Requires:         R-CRAN-EbayesThresh >= 1.3.2

%description
This package carries out level-dependent cross-validation method for the
selection of thresholding value in wavelet shrinkage. This procedure is
implemented by coupling a conventional cross validation with an imputation
method due to a limitation of data length, a power of 2. It can be easily
applied to classical leave-one-out and k-fold cross validation. Since the
procedure is computationally fast, a level-dependent cross validation can
be performed for wavelet shrinkage of various data such as a data with
correlated errors.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
