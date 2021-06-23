%global __brp_check_rpaths %{nil}
%global packname  CornerstoneR
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Scripts for Interface Between 'Cornerstone' and'R'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 1.9.1
BuildRequires:    R-CRAN-data.table >= 1.10
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-SpatialTools 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-checkmate >= 1.9.1
Requires:         R-CRAN-data.table >= 1.10
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-SpatialTools 
Requires:         R-CRAN-vcd 

%description
Collection of generic 'R' scripts which enable you to use existing 'R'
routines in 'Cornerstone'.

The desktop application 'Cornerstone'
(<https://www.camline.com/en/products/cornerstone/cornerstone-core.html>)
is a data analysis software provided by 'camLine' that empowers
engineering teams to find solutions even faster. The engineers incorporate
intensified hands-on statistics into their projects. They benefit from an
intuitive and uniquely designed graphical Workmap concept: you design
experiments (DoE) and explore data, analyze dependencies, and find answers
you can act upon, immediately, interactively, and without any programming.

While 'Cornerstone's' interface to the statistical programming language
'R' has been available since version 6.0, the latest interface with 'R' is
even much more efficient. 'Cornerstone' release 7.1.1 allows you to
integrate user defined 'R' packages directly into the standard
'Cornerstone' GUI. Your engineering team stays in 'Cornerstone's'
graphical working environment and can apply 'R' routines, immediately and
without the need to deal with programming code. Additionally, your 'R'
programming team develops corresponding 'R' packages detached from
'Cornerstone' in their favorite 'R' environment.

Learn how to use 'R' packages in 'Cornerstone' 7.1.1 on 'camLineTV'
YouTube channel (<https://www.youtube.com/watch?v=HEQHwq_laXU>) (available
in German).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
