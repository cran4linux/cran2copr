%global __brp_check_rpaths %{nil}
%global packname  fdANOVA
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis of Variance for Univariate and Multivariate FunctionalData

License:          LGPL-2 | LGPL-3 | GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-doBy 
Requires:         R-MASS 
Requires:         R-CRAN-magic 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 

%description
Performs analysis of variance testing procedures for univariate and
multivariate functional data (Cuesta-Albertos and Febrero-Bande (2010)
<doi:10.1007/s11749-010-0185-3>, Gorecki and Smaga (2015)
<doi:10.1007/s00180-015-0555-0>, Gorecki and Smaga (2017)
<doi:10.1080/02664763.2016.1247791>, Zhang et al. (2018)
<doi:10.1016/j.csda.2018.05.004>).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
