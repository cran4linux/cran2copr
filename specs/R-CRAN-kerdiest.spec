%global __brp_check_rpaths %{nil}
%global packname  kerdiest
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric kernel estimation of the distribution function.Bandwidth selection and estimation of related functions.

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-date 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-CRAN-evir 
Requires:         R-CRAN-date 
Requires:         R-CRAN-chron 
Requires:         R-CRAN-evir 

%description
Nonparametric kernel distribution function estimation is performed. Three
automatic bandwidth selection methods for nonparametric kernel
distribution function estimation are implemented: the plug-in of Altman
and Leger, the plug-in of Polansky and Baker, and the modified
cross-validation of Bowman, Hall and Prvan. The exceedance function, the
mean return period and the return level are also computed.

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
%{rlibdir}/%{packname}/INDEX
