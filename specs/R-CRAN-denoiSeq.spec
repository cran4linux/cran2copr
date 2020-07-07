%global packname  denoiSeq
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Differential Expression Analysis Using a Bottom-Up Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Given count data from two conditions, it determines which transcripts are
differentially expressed across the two conditions using Bayesian
inference of the parameters of a bottom-up model for PCR amplification.
This model is developed in Ndifon Wilfred, Hilah Gal, Eric Shifrut, Rina
Aharoni, Nissan Yissachar, Nir Waysbort, Shlomit Reich Zeliger, Ruth
Arnon, and Nir Friedman (2012),
<http://www.pnas.org/content/109/39/15865.full>, and results in a
distribution for the counts that is a superposition of the binomial and
negative binomial distribution.

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
