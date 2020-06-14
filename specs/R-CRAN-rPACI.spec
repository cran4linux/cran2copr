%global packname  rPACI
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Placido Analysis of Corneal Irregularity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Analysis of corneal data obtained from a Placido disk corneal topographer
with calculation of irregularity indices. A corneal topographer is an
ophthalmic clinical device that obtains measurements in the cornea (the
anterior part of the eye). A Placido disk corneal topographer makes use of
the Placido disk (Rowsey et al. (1981),
<doi:10.1001/archopht.1981.03930011093022>, Rand et al. (1997),
<doi:10.1016/S0886-3350(99)00355-7>), which produce a circular pattern of
measurement nodes. The raw information measured by such a topographer is
used by practitioners to analyze curvatures, to study optical aberrations,
or to diagnose specific conditions of the eye. The rPACI package allows
the calculation of the corneal irregularity indices described in
Ramos-Lopez et al. (2013), <doi:10.1097/OPX.0b013e3182843f2a>, and that
were firstly introduced in Ramos-Lopez et al. (2011),
<doi:10.1097/OPX.0b013e3182843f2a>. It provides a simple interface to read
corneal topography data files as exported by a typical Placido disk
topographer, to compute the irregularity indices mentioned before, and to
display summary plots that are easy to interpret for a clinician.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
