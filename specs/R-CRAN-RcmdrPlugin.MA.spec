%global packname  RcmdrPlugin.MA
%global packver   0.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          2%{?dist}
Summary:          Graphical User Interface for Conducting Meta-Analyses in R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr 
BuildRequires:    R-CRAN-MAd 
BuildRequires:    R-CRAN-metafor 
Requires:         R-CRAN-Rcmdr 
Requires:         R-CRAN-MAd 
Requires:         R-CRAN-metafor 

%description
Easy to use interface for conducting meta-analysis in R. This package is
an Rcmdr-plugin, which allows the user to conduct analyses in a
menu-driven, graphical user interface environment (e.g., CMA, SPSS). It
uses recommended procedures as described in The Handbook of Research
Synthesis and Meta-Analysis (Cooper, Hedges, & Valentine, 2009).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
