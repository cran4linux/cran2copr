%global __brp_check_rpaths %{nil}
%global packname  fluspect
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fluspect-B

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
Requires:         R-CRAN-pracma 
Requires:         R-utils 

%description
A model for leaf fluorescence, reflectance and transmittance spectra. It
implements the model introduced by Vilfan et al. (2016)
<DOI:10.1016/j.rse.2016.09.017>. Fluspect-B calculates the emission of
ChlF on both the illuminated and shaded side of the leaf. Other input
parameters are chlorophyll and carotenoid concentrations, leaf water, dry
matter and senescent material (brown pigments) content, leaf mesophyll
structure parameter and ChlF quantum efficiency for the two photosystems,
PS-I and PS-II.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
