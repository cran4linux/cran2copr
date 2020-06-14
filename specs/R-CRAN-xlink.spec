%global packname  xlink
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Genetic Association Models for X-Chromosome SNPS on Continuous,Binary and Survival Outcomes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-survival >= 2.41.3
Requires:         R-survival >= 2.41.3

%description
The expression of X-chromosome undergoes three possible biological
processes: X-chromosome inactivation (XCI), escape of the X-chromosome
inactivation (XCI-E),and skewed X-chromosome inactivation (XCI-S). To
analyze the X-linked genetic association for phenotype such as continuous,
binary, and time-to-event outcomes with the actual process unknown, we
propose a unified approach of maximizing the likelihood or partial
likelihood over all of the potential biological processes. The methods are
described in Wei Xu, Meiling Hao (2017) <doi:10.1002/gepi.22097>. And also
see Dongxiao Han, Meiling Hao, Lianqiang Qu, Wei Xu (2019)
<doi:10.1177/0962280219859037>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
