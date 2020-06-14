%global packname  Orcs
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Omnidirectional R Code Snippets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
Requires:         p7zip
Requires:         dos2unix
BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-bookdown 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-knitr 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sp 
Requires:         R-stats 

%description
I tend to repeat the same code chunks over and over again. At first, this
was fine for me and I paid little attention to such redundancies. A little
later, when I got tired of manually replacing Linux filepaths with the
referring Windows versions, and vice versa, I started to stuff some very
frequently used work-steps into functions and, even later, into a proper R
package. And that's what this package is - a hodgepodge of various R
functions meant to simplify (my) everyday-life coding work without, at the
same time, being devoted to a particular scope of application.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
