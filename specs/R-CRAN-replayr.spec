%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  replayr
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Read Input Recordings of Video Games

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 3.0.2
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
Requires:         R-CRAN-zip >= 3.0.2
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-xml2 
Requires:         R-utils 

%description
Imports input recordings and demo files of video games, as made in
tool-assisted speedrunning, reinforcement learning, and research on
human-game interaction. Reads the formats of 'FCEUX', 'BizHawk',
'Dolphin', 'Citra', 'libTAS', 'openMSX', 'JPC-RR', 'Gym Retro', the 'Doom'
and 'GoldSrc' engines, and other recording tools. Platforms include the
Atari 2600, Nintendo, Sega, and Sony consoles, arcade machines, and
personal computers. Imported recordings keep compact digital control
arrays, stable control identities, original numeric channels, metadata,
and emulator commands. Supports gamepads, keyboards, mice, touchscreens,
and recorded motion or light-gun channels. Source timing distinguishes
frames, controller polls, and timestamped events. Left and right stick
directions, angles, and magnitudes can be selected independently. Allows
analysis of input recordings without running an emulator.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
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
