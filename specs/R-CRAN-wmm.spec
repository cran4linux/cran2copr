%global packname  wmm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          World Magnetic Model

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Calculate magnetic field at a given location and time according to the
World Magnetic Model (WMM). Both the main field and secular variation
components are returned. This functionality is useful for physicists and
geophysicists who need orthogonal components from WMM. Currently, this
package supports annualized time inputs between 2000 and 2020. If desired,
users can specify which WMM version to use, e.g., the original WMM2015
release or the recent out-of-cycle WMM2015 release. Methods used to
implement WMM, including the Gauss coefficients for each release, are
described in the following publications: Chulliat et al (2019)
<doi:10.25921/xhr3-0t19>, Chulliat et al (2015) <doi:10.7289/V5TB14V7>,
Maus et al (2010)
<https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/WMM2010_Report.pdf>,
McLean et al (2004)
<https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/TRWMM_2005.pdf>, and
Macmillian et al (2000)
<https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/wmm2000.pdf>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
