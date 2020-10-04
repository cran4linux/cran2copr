%global packname  transmem
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Treatment of Membrane-Transport Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cmna 
BuildRequires:    R-CRAN-ggformula 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-cmna 
Requires:         R-CRAN-ggformula 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plot3D 

%description
Treatment and visualization of membrane (selective) transport data.
Transport profiles involving up to three species are produced as
publication-ready plots and several membrane performance parameters (e.g.
separation factors as defined in Koros et al. (1996)
<doi:10.1351/pac199668071479> and non-linear regression parameters for the
equations described in Rodriguez de San Miguel et al. (2014)
<doi:10.1016/j.jhazmat.2014.03.052>) can be obtained. Many widely used
experimental setups (e.g. membrane physical aging) can be easily studied
through the package's graphical representations.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
