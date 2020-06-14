%global packname  TVMM
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          2%{?dist}
Summary:          Multivariate Tests for the Vector of Means

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-DescToolsAddIns 
Requires:         R-tcltk 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-tkrplot 
Requires:         R-CRAN-gridExtra 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-CRAN-DescToolsAddIns 

%description
This is a statistical tool interactive that provides multivariate
statistical tests that are more powerful than traditional Hotelling T2
test and LRT (likelihood ratio test) for the vector of normal mean
populations with and without contamination and non-normal populations
(Henrique J. P. Alves & Daniel F. Ferreira (2019) <DOI:
10.1080/03610918.2019.1693596>).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/INDEX
