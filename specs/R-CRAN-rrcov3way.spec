%global __brp_check_rpaths %{nil}
%global packname  rrcov3way
%global packver   0.1-18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.18
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Methods for Multiway Data Analysis, Applicable also forCompositional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-nnls 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-nnls 

%description
Provides methods for multiway data analysis by means of Parafac and Tucker
3 models. Robust versions (Engelen and Hubert (2011)
<doi:10.1016/j.aca.2011.04.043>) and versions for compositional data are
also provided (Gallo (2015) <doi:10.1080/03610926.2013.798664>, Di Palma
et al. (2018) <doi:10.1080/02664763.2017.1381669>.

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
