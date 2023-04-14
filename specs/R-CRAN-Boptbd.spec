%global __brp_check_rpaths %{nil}
%global packname  Boptbd
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Optimal Block Designs

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-tcltk 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-tcltk 

%description
Computes Bayesian A- and D-optimal block designs under the linear mixed
effects model settings using block/array exchange algorithm of Debusho,
Gemechu and Haines (2018) <doi:10.1080/03610918.2018.1429617> where the
interest is in a comparison of all possible elementary treatment
contrasts. The package also provides an optional method of using the
graphical user interface (GUI) R package 'tcltk' to ensure that it is user
friendly.

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
