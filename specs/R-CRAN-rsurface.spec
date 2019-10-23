%global packname  rsurface
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Design of Rotatable Central Composite Experiments and ResponseSurface Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-rsm 
BuildRequires:    R-stats 
Requires:         R-grDevices 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-rsm 
Requires:         R-stats 

%description
Produces tables with the level of replication (number of replicates) and
the experimental uncoded values of the quantitative factors to be used for
rotatable Central Composite Design (CCD) experimentation and a 2-D contour
plot of the corresponding variance of the predicted response according to
Mead et al. (2012) <doi:10.1017/CBO9781139020879> design_ccd(), and
analyzes CCD data with response surface methodology ccd_analysis(). A
rotatable CCD provides values of the variance of the predicted response
that are concentrically distributed around the average treatment
combination used in the experimentation, which with uniform precision
(implied by the use of several replicates at the average treatment
combination) improves greatly the search and finding of an optimum
response. These properties of a rotatable CCD represent undeniable
advantages over the classical factorial design, as discussed by Panneton
et al. (1999) <doi:10.13031/2013.13267> and Mead et al. (2012)
<doi:10.1017/CBO9781139020879.018> among others.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
