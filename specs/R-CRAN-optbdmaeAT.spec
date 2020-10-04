%global packname  optbdmaeAT
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Optimal Block Designs for Two-Colour cDNA Microarray Experiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
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
Computes A-, MV-, D- and E-optimal or near-optimal block designs for
two-colour cDNA microarray experiments using the linear fixed effects and
mixed effects models where the interest is in a comparison of all possible
elementary treatment contrasts. The algorithms used in this package are
based on the treatment exchange and array exchange algorithms of Debusho,
Gemechu and Haines (2016, unpublished). The package also provides an
optional method of using the graphical user interface (GUI) R package
tcltk to ensure that it is user friendly.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
