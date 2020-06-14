%global packname  dplRCon
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Concordance for Dendroclimatology

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
The concordance method is a non-parametric method based on bootstrapping
that is used to test the hypothesis that two subsets of time series are
similar in terms of mean, variance or both. This method was developed to
address a concern within dendroclimatology that young trees may produce a
differing climate response to older more established trees. Details of
this method are available in Pirie, M. (2013). The Climate of New Zealand
reconstructed from kauri tree rings: Enhancement through the use of novel
statistical methodology. PhD. Dissertation, School of Environment and
Department of Statistics, University of Auckland, New Zealand. This
package also produces a figure with 3 panels, each panel is for a
different climate variable. An example of this figure in included in "On
the influence of tree size on the climate - growth relationship of New
Zealand kauri (Agathis australis): insights from annual, monthly and daily
growth patterns. J Wunder, AM Fowler, ER Cook, M Pirie, SPJ McCloskey.
Trees 27 (4), 937-948". For further R functions for loading your own
dendroclimatology datasets and performing dendrochronology analysis refer
to the R package "dplR: Dendrochronology Program Library in R". The
concordance procedure is intended to add to the standard dendrochronology
techniques provided in "dplR".

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
