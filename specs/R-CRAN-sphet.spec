%global __brp_check_rpaths %{nil}
%global packname  sphet
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of Spatial Autoregressive Models with and withoutHeteroscedasticity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-spdep >= 0.5.67
BuildRequires:    R-nlme 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-methods 
Requires:         R-CRAN-spdep >= 0.5.67
Requires:         R-nlme 
Requires:         R-Matrix 
Requires:         R-CRAN-sp 
Requires:         R-methods 

%description
Generalized Method of Moment estimation of Cliff-Ord-type spatial
autoregressive models with and without Heteroscedasticity.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
