%global packname  optrcdmaeAT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Optimal Row-Column Designs for Two-Colour cDNA MicroarrayExperiments

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
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
Computes A-, MV-, D- and E-optimal or near-optimal row-column designs for
two-colour cDNA microarray experiments using the linear fixed effects and
mixed effects models where the interest is in a comparison of all pairwise
treatment contrasts. The algorithms used in this package are based on the
array exchange and treatment exchange algorithms adopted from Debusho,
Gemechu and Haines (2016, unpublished) algorithms after adjusting for the
row-column designs setup. The package also provides an optional method of
using the graphical user interface (GUI) R package tcltk to ensure that it
is user friendly.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
