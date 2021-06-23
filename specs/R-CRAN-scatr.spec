%global __brp_check_rpaths %{nil}
%global packname  scatr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Create Scatter Plots with Marginal Density or Box Plots

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jmvcore >= 0.8.0
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-ggstance 
BuildRequires:    R-CRAN-ggridges 
Requires:         R-CRAN-jmvcore >= 0.8.0
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-ggstance 
Requires:         R-CRAN-ggridges 

%description
Allows you to make clean, good-looking scatter plots with the option to
easily add marginal density or box plots on the axes. It is also available
as a module for 'jamovi' (see <https://www.jamovi.org> for more
information). 'Scatr' is based on the 'cowplot' package by Claus O. Wilke
and the 'ggplot2' package by Hadley Wickham.

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
