%global packname  NDP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Presentation for Working with Normal Distribution

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-rmarkdown 

%description
An interactive presentation on the topic of normal distribution using
'rmarkdown' and 'shiny' packages. It is helpful to those who want to learn
normal distribution quickly and get a hands on experience. The
presentation has a template for solving problems on normal distribution.
Runtime examples are provided in the package function as well as at
<https://kartikeyastat.shinyapps.io/NormalDistribution/>.

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
%doc %{rlibdir}/%{packname}/img
%doc %{rlibdir}/%{packname}/N.Rmd
%doc %{rlibdir}/%{packname}/SF.JPG
%doc %{rlibdir}/%{packname}/VC.jpg
%{rlibdir}/%{packname}/INDEX
