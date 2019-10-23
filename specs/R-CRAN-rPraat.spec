%global packname  rPraat
%global packver   1.2.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0.2
Release:          1%{?dist}
Summary:          Interface to Praat

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-graphics >= 3.1.0
BuildRequires:    R-CRAN-tuneR >= 1.3.3
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-readr >= 1.2.1
BuildRequires:    R-CRAN-dygraphs >= 1.1.1.6
BuildRequires:    R-CRAN-dplyr >= 0.7.8
Requires:         R-graphics >= 3.1.0
Requires:         R-CRAN-tuneR >= 1.3.3
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-readr >= 1.2.1
Requires:         R-CRAN-dygraphs >= 1.1.1.6
Requires:         R-CRAN-dplyr >= 0.7.8

%description
Read, write and manipulate 'Praat' TextGrid, PitchTier, Pitch,
IntensityTier, Formant, and Collection files
<http://www.fon.hum.uva.nl/praat/>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
