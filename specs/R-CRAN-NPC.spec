%global __brp_check_rpaths %{nil}
%global packname  NPC
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Nonparametric Combination of Hypothesis Tests

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-coin 
BuildRequires:    R-CRAN-matlab 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-coin 
Requires:         R-CRAN-matlab 

%description
An implementation of nonparametric combination of hypothesis tests. This
package performs nonparametric combination (Pesarin and Salmaso 2010), a
permutation-based procedure for jointly testing multiple hypotheses. The
tests are conducted under the global "sharp" null hypothesis of no
effects, and the component tests are combined on the metric of their
p-values. A key feature of nonparametric combination is that it accounts
for the dependence among tests under the null hypothesis. In addition to
the "NPC" function, which performs nonparametric combination itself, the
package also contains a number of helper functions, many of which
calculate a test statistic given an input of data.

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
%{rlibdir}/%{packname}/INDEX
