%global __brp_check_rpaths %{nil}
%global packname  simba
%global packver   0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          3%{?dist}%{?buildtag}
Summary:          A Collection of functions for similarity analysis of vegetationdata

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.0
Requires:         R-core >= 2.12.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-vegan 
Requires:         R-stats 
Requires:         R-CRAN-vegan 

%description
Besides functions for the calculation of similarity and multiple plot
similarity measures with binary data (for instance presence/absence
species data) the package contains some simple wrapper functions for
reshaping species lists into matrices and vice versa and some other
functions for further processing of similarity data (Mantel-like
permutation procedures) as well as some other useful stuff for vegetation
analysis.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
