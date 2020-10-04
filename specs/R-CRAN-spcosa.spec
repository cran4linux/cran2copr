%global packname  spcosa
%global packver   0.3-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          3%{?dist}%{?buildtag}
Summary:          Spatial Coverage Sampling and Random Sampling from CompactGeographical Strata

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.1.0
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-rJava >= 0.9.3
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp >= 1.1.0
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-rJava >= 0.9.3
Requires:         R-methods 
Requires:         R-utils 

%description
Spatial coverage sampling and random sampling from compact geographical
strata created by k-means. See Walvoort et al. (2010)
<doi:10.1016/j.cageo.2010.04.005> for details.

%prep
%setup -q -c -n %{packname}
sed -i '/Sexpr/d' %{packname}/man/spcosa-package.Rd

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/FAQ
%doc %{rlibdir}/%{packname}/java
%doc %{rlibdir}/%{packname}/maps
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
