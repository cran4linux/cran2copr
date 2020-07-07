%global packname  passt
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Probability Associator Time (PASS-T)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 

%description
Simulates judgments of frequency and duration based on the Probability
Associator Time (PASS-T) model. PASS-T is a memory model based on a simple
competitive artificial neural network. It can imitate human judgments of
frequency and duration, which have been extensively studied in cognitive
psychology (e.g. Hintzman (1970) <doi:10.1037/h0028865>, Betsch et al.
(2010) <https://psycnet.apa.org/record/2010-18204-003>). The PASS-T model
is an extension of the PASS model (Sedlmeier, 2002, ISBN:0198508638). The
package provides an easy way to run simulations, which can then be
compared with empirical data in human judgments of frequency and duration.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
