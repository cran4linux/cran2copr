%global packname  rsleep
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Analysis of Sleep Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-edfReader 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-phonTools 
Requires:         R-CRAN-edfReader 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-phonTools 

%description
Provides users functions for sleep data management and analysis such as
European Data Format (EDF) to Morpheo Data Format (MDF) conversion:
P.Bouchequet, D.Jin, G.Solelhac, M.Chennaoui, D.Leger (2018)
<doi:10.1016/j.msom.2018.01.130> "Morpheo Data Format (MDF), un nouveau
format de donnees simple, robuste et performant pour stocker et analyser
les enregistrements de sommeil". Provides hypnogram statistics computing
and visualisation functions from the American Academy of Sleep Medicine
(AASM) manual "The AASM Manual for the Scoring of Sleep and Associated
Events" <https://aasm.org/clinical-resources/scoring-manual/>.

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
