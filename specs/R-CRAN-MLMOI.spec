%global packname  MLMOI
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Estimating Frequencies, Prevalence and Multiplicity of Infection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.10
BuildRequires:    R-CRAN-Rmpfr >= 0.7.1
BuildRequires:    R-CRAN-XLConnect >= 0.2.15
BuildRequires:    R-CRAN-Rdpack >= 0.10.1
Requires:         R-CRAN-rJava >= 0.9.10
Requires:         R-CRAN-Rmpfr >= 0.7.1
Requires:         R-CRAN-XLConnect >= 0.2.15
Requires:         R-CRAN-Rdpack >= 0.10.1

%description
The implemented methods reach out to scientists that seek to estimate
multiplicity of infection (MOI) and lineage (allele) frequencies and
prevalences at molecular markers using the maximum-likelihood method
described in Schneider (2018) <doi:10.1371/journal.pone.0194148>, and
Schneider and Escalante (2014) <doi:10.1371/journal.pone.0097899>. Users
can import data from Excel files in various formats, and perform
maximum-likelihood estimation on the imported data by the package's
moimle() function.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
