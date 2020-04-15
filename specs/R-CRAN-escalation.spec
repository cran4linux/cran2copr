%global packname  escalation
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Modular Approach to Dose Finding Clinical Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-CRAN-BOIN 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-tidyr >= 1.0
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-dfcrm 
Requires:         R-CRAN-BOIN 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-viridis 

%description
Methods for working with dose-finding clinical trials. We start by
providing a common interface to various dose-finding methodologies like
the continual reassessment method (CRM) by O'Quigley et al. (1990)
<doi:10.2307/2531628>, the Bayesian optimal interval design (BOIN) by Liu
& Yuan (2015) <doi:10.1111/rssc.12089>, and the 3+3 described by Korn et
al. (1994) <doi:10.1002/sim.4780131802>. We then add optional
embellishments to provide extra desirable behaviour, like avoiding
skipping doses, stopping after n patients have been treated at the
recommended dose, or demanding that n patients are treated before stopping
is allowed. By daisy-chaining together these embellishments using the pipe
operator from 'magrittr', it is simple to tailor the behaviour of
dose-finding designs so that they do what you want. Furthermore, using
this flexible interface for creating dose-finding designs, it is simple to
run simulations or calculate dose-pathways for future cohorts of patients.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
