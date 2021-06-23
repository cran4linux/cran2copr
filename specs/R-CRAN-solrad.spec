%global __brp_check_rpaths %{nil}
%global packname  solrad
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Calculating Solar Radiation and Related Variables Based onLocation, Time and Topographical Conditions

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch

%description
For surface energy models and estimation of solar positions and components
with varying topography, time and locations. The functions calculate solar
top-of-atmosphere, open, diffuse and direct components, atmospheric
transmittance and diffuse factors, day length, sunrise and sunset, solar
azimuth, zenith, altitude, incidence, and hour angles, earth declination
angle, equation of time, and solar constant. Details about the methods and
equations are explained in Seyednasrollah, Bijan, Mukesh Kumar, and
Timothy E. Link. 'On the role of vegetation density on net snow cover
radiation at the forest floor.' Journal of Geophysical Research:
Atmospheres 118.15 (2013): 8359-8374, <doi:10.1002/jgrd.50575>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
