%global packname  celltrackR
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Motion Trajectory Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ellipse 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-CRAN-ellipse 

%description
Provides methodology to analyze cells that move in a two- or
three-dimensional space. Available measures include displacement,
confinement ratio, autocorrelation, straightness, turning angle, and
fractal dimension. Measures can be applied to entire tracks, steps, or
subtracks with varying length. While the methodology has been developed
for cell trajectory analysis, it is applicable to anything that moves
including animals, people, or vehicles. Some of the methodology
implemented in this packages was described by: Beauchemin, Dixit, and
Perelson (2007) <doi:10.4049/jimmunol.178.9.5505>, Beltman, Maree, and de
Boer (2009) <doi:10.1038/nri2638>, Gneiting and Schlather (2004)
<doi:10.1137/S0036144501394387>, Mokhtari, Mech, Zitzmann, Hasenberg,
Gunzer, and Figge (2013) <doi:10.1371/journal.pone.0080808>, Moreau,
Lemaitre, Terriac, Azar, Piel, Lennon-Dumenil, and Bousso (2012)
<doi:10.1016/j.immuni.2012.05.014>, Textor, Peixoto, Henrickson, Sinn, von
Andrian, and Westermann (2011) <doi:10.1073/pnas.1102288108>, Textor,
Sinn, and de Boer (2013) <doi:10.1186/1471-2105-14-S6-S10>, Textor,
Henrickson, Mandl, von Andrian, Westermann, de Boer, and Beltman (2014)
<doi:10.1371/journal.pcbi.1003752>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/learnmore
%{rlibdir}/%{packname}/INDEX
