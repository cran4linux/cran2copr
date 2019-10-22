%global packname  robustDA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Robust Mixture Discriminant Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-Rsolnp 

%description
Robust mixture discriminant analysis (RMDA, Bouveyron & Girard, 2009)
allows to build a robust supervised classifier from learning data with
label noise. The idea of the proposed method is to confront an
unsupervised modeling of the data with the supervised information carried
by the labels of the learning data in order to detect inconsistencies. The
method is able afterward to build a robust classifier taking into account
the detected inconsistencies into the labels.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
