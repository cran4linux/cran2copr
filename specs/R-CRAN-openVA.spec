%global packname  openVA
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          3%{?dist}
Summary:          Automated Method for Verbal Autopsy

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-InterVA4 >= 1.7.3
BuildRequires:    R-CRAN-InSilicoVA >= 1.1.3
BuildRequires:    R-CRAN-InterVA5 >= 1.0.1
BuildRequires:    R-CRAN-Tariff >= 1.0.1
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-methods 
Requires:         R-CRAN-InterVA4 >= 1.7.3
Requires:         R-CRAN-InSilicoVA >= 1.1.3
Requires:         R-CRAN-InterVA5 >= 1.0.1
Requires:         R-CRAN-Tariff >= 1.0.1
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-cli 
Requires:         R-methods 

%description
Implements multiple existing open-source algorithms for coding cause of
death from verbal autopsies. The methods implemented include 'InterVA4' by
Byass et al (2012) <doi:10.3402/gha.v5i0.19281>, 'InterVA5' by Byass at al
(2019) <doi:10.1186/s12916-019-1333-6>, 'InSilicoVA' by McCormick et al
(2016) <doi:10.1080/01621459.2016.1152191>, 'NBC' by Miasnikof et al
(2015) <doi:10.1186/s12916-015-0521-2>, and a replication of 'Tariff'
method by James et al (2011) <doi:10.1186/1478-7954-9-31> and Serina, et
al. (2015) <doi:10.1186/s12916-015-0527-9>. It also provides tools for
data manipulation tasks commonly used in Verbal Autopsy analysis and
implements easy graphical visualization of individual and population level
statistics. The 'NBC' method is implemented by the 'nbc4va' package that
can be installed from <https://github.com/rrwen/nbc4va>. Note that this
package was not developed by authors affiliated with the Institute for
Health Metrics and Evaluation and thus unintentional discrepancies may
exist in the implementation of the 'Tariff' method.

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
%{rlibdir}/%{packname}/INDEX
