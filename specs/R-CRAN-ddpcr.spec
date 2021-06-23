%global __brp_check_rpaths %{nil}
%global packname  ddpcr
%global packver   1.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.15
Release:          3%{?dist}%{?buildtag}
Summary:          Analysis and Visualization of Droplet Digital PCR in R and onthe Web

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-plyr >= 1.8.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-mixtools >= 1.0.2
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-shinyjs >= 0.4
BuildRequires:    R-CRAN-DT >= 0.2
BuildRequires:    R-CRAN-shiny >= 0.11.0
BuildRequires:    R-CRAN-lazyeval >= 0.1.10
BuildRequires:    R-CRAN-readr >= 0.1.0
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-plyr >= 1.8.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-mixtools >= 1.0.2
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-shinyjs >= 0.4
Requires:         R-CRAN-DT >= 0.2
Requires:         R-CRAN-shiny >= 0.11.0
Requires:         R-CRAN-lazyeval >= 0.1.10
Requires:         R-CRAN-readr >= 0.1.0
Requires:         R-CRAN-tibble 

%description
An interface to explore, analyze, and visualize droplet digital PCR
(ddPCR) data in R. This is the first non-proprietary software for
analyzing two-channel ddPCR data. An interactive tool was also created and
is available online to facilitate this analysis for anyone who is not
comfortable with using R.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/sample_data
%doc %{rlibdir}/%{packname}/shiny
%doc %{rlibdir}/%{packname}/vignette_files
%doc %{rlibdir}/%{packname}/vignettes-supp
%{rlibdir}/%{packname}/INDEX
