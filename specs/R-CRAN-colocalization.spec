%global packname  colocalization
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Normalized Spatial Intensity Correlation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Calculate the colocalization index, NSInC, in two different ways as
described in the paper (Liu et al., 2018. Manuscript submitted for
publication.) for multiple-species spatial data which contain the precise
locations and membership of each spatial point. The two main functions are
nsinc.d() and nsinc.z(). They provide the Pearson’s correlation
coefficients of signal proportions in different memberships within a
concerned proximity of every signal (or every base signal if single
direction colocalization is considered) across all (base) signals using
two different ways of normalization. The proximity sizes could be an
individual value or a range of values, where the default ranges of values
are different for the two functions.

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
