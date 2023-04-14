%global __brp_check_rpaths %{nil}
%global packname  conicfit
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Algorithms for Fitting Circles, Ellipses and Conics Based on theWork by Prof. Nikolai Chernov

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.7.0
Requires:         R-core >= 2.7.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-geigen 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-geigen 

%description
Geometric circle fitting with Levenberg-Marquardt (a, b, R),
Levenberg-Marquardt reduced (a, b), Landau, Spath and Chernov-Lesort.
Algebraic circle fitting with Taubin, Kasa, Pratt and
Fitzgibbon-Pilu-Fisher. Geometric ellipse fitting with ellipse LMG
(geometric parameters) and conic LMA (algebraic parameters). Algebraic
ellipse fitting with Fitzgibbon-Pilu-Fisher and Taubin.

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
