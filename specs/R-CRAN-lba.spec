%global __brp_check_rpaths %{nil}
%global packname  lba
%global packver   2.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4.4
Release:          3%{?dist}%{?buildtag}
Summary:          Latent Budget Analysis for Compositional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-rgl 
Requires:         R-MASS 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-rgl 

%description
Latent budget analysis is a method for the analysis of a two-way
contingency table with an exploratory variable and a response variable. It
is specially designed for compositional data.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
