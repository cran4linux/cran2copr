%global __brp_check_rpaths %{nil}
%global packname  dosedesignR
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          3%{?dist}%{?buildtag}
Summary:          Interactive Designing of Dose Finding Studies

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DoseFinding 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DoseFinding 
Requires:         R-CRAN-DT 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 

%description
Provides the user with an interactive application which can be used to
facilitate the planning of dose finding studies by applying the theory of
optimal experimental design (e.g., Ling (2006)
<doi:10.1007/0-387-33706-7>).

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny-app
%{rlibdir}/%{packname}/INDEX
