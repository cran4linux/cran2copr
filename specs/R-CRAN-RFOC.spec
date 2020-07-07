%global packname  RFOC
%global packver   3.4-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.6
Release:          3%{?dist}
Summary:          Graphics for Spherical Distributions and Earthquake FocalMechanisms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RPMG 
BuildRequires:    R-CRAN-GEOmap 
BuildRequires:    R-CRAN-RSEIS 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-splancs 
Requires:         R-CRAN-RPMG 
Requires:         R-CRAN-GEOmap 
Requires:         R-CRAN-RSEIS 
Requires:         R-MASS 
Requires:         R-CRAN-splancs 

%description
Graphics for statistics on a sphere, as applied to geological fault data,
crystallography, earthquake focal mechanisms, radiation patterns, ternary
plots and geographical/geological maps.  Non-double couple plotting of
focal spheres and source type maps are included for statistical analysis
of moment tensors.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
