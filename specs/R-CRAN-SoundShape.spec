%global packname  SoundShape
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sound Waves Onto Morphometric Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-geomorph >= 3.0.2
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-seewave 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-utils 
Requires:         R-CRAN-geomorph >= 3.0.2
Requires:         R-CRAN-abind 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-seewave 
Requires:         R-stats 
Requires:         R-CRAN-tuneR 
Requires:         R-utils 

%description
Implement a promising, and yet little explored protocol for bioacoustical
analysis, the eigensound method by MacLeod, Krieger and Jones (2013)
<doi:10.4404/hystrix-24.1-6299>. Eigensound is a multidisciplinary method
focused on the direct comparison between stereotyped sounds from different
species. 'SoundShape', in turn, provide the tools required for anyone to
go from sound waves to Principal Components Analysis, using tools
extracted from traditional bioacoustics (i.e. 'tuneR' and 'seewave'
packages), geometric morphometrics (i.e. 'geomorph' package) and
multivariate analysis (e.g. 'stats' package). For more information, please
see Rocha and Romano (in prep) and check 'SoundShape' repository on GitHub
for news and updates <https://github.com/p-rocha/SoundShape>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
