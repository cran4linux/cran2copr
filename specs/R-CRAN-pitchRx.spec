%global __brp_check_rpaths %{nil}
%global packname  pitchRx
%global packver   1.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8.2
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Harnessing 'MLBAM' 'Gameday' Data and Visualizing'pitchfx'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3
BuildRequires:    R-CRAN-XML2R >= 0.0.6
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-hexbin 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-ggplot2 >= 0.9.3
Requires:         R-CRAN-XML2R >= 0.0.6
Requires:         R-CRAN-plyr 
Requires:         R-MASS 
Requires:         R-CRAN-hexbin 
Requires:         R-mgcv 

%description
With 'pitchRx', one can easily obtain Major League Baseball Advanced
Media's 'Gameday' data (as well as store it in a remote database). The
'Gameday' website hosts a wealth of data in XML format, but perhaps most
interesting is 'pitchfx'. Among other things, 'pitchfx' data can be used
to recreate a baseball's flight path from a pitcher's hand to home plate.
With pitchRx, one can easily create animations and interactive 3D
'scatterplots' of the baseball's flight path. 'pitchfx' data is also
commonly used to generate a static plot of baseball locations at the
moment they cross home plate. These plots, sometimes called strike-zone
plots, can also refer to a plot of event probabilities over the same
region. 'pitchRx' provides an easy and robust way to generate strike-zone
plots using the 'ggplot2' package.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
