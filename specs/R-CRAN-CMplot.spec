%global packname  CMplot
%global packver   3.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.3
Release:          1%{?dist}
Summary:          Circle Manhattan Plot

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Manhattan plot, a type of scatter plot, was widely used to display the
association results. However, it is usually time-consuming and laborious
for a non-specialist user to write scripts and adjust parameters of an
elaborate plot. Moreover, the ever-growing traits measured have
necessitated the integration of results from different Genome-wide
association study researches. Circle Manhattan Plot is the first open R
package that can lay out Genome-wide association study P-value results in
both traditional rectangular patterns, QQ-plot and novel circular ones.
United in only one bull's eye style plot, association results from
multiple traits can be compared interactively, thereby to reveal both
similarities and differences between signals.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
