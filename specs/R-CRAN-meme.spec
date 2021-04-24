%global packname  meme
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Create Meme

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-magick 
Requires:         R-methods 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-sysfonts 
Requires:         R-utils 

%description
The word 'Meme' was originated from the book, 'The Selfish Gene', authored
by Richard Dawkins (1976). It is a unit of culture that is passed from one
generation to another and correlates to the gene, the unit of physical
heredity. The internet memes are captioned photos that are intended to be
funny, ridiculous. Memes behave like infectious viruses and travel from
person to person quickly through social media. The 'meme' package allows
users to make custom memes.

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
