%global packname  permute
%global packver   0.9-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.5
Release:          3%{?dist}
Summary:          Functions for Generating Restricted Permutations of Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
A set of restricted permutation designs for freely exchangeable, line
transects (time series), and spatial grid designs plus permutation of
blocks (groups of samples) is provided. 'permute' also allows split-plot
designs, in which the whole-plots or split-plots or both can be
freely-exchangeable or one of the restricted designs. The 'permute'
package is modelled after the permutation schemes of 'Canoco 3.1' (and
later) by Cajo ter Braak.

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
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/TODO.md
%{rlibdir}/%{packname}/INDEX
