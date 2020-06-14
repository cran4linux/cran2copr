%global packname  tdigest
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Wicked Fast, Accurate Quantiles Using t-Digests

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 

%description
The t-Digest construction algorithm, by Dunning et al., (2019)
<arXiv:1902.04023v1>, uses a variant of 1-dimensional k-means clustering
to produce a very compact data structure that allows accurate estimation
of quantiles. This t-Digest data structure can be used to estimate
quantiles, compute other rank statistics or even to estimate related
measures like trimmed means. The advantage of the t-Digest over previous
digests for this purpose is that the t-Digest handles data with full
floating point resolution. The accuracy of quantile estimates produced by
t-Digests can be orders of magnitude more accurate than those produced by
previous digest algorithms. Methods are provided to create and update
t-Digests and retrieve quantiles from the accumulated distributions.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
