%global packname  sparseIndexTracking
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Design of Portfolio of Stocks to Track an Index

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computation of sparse portfolios for financial index tracking, i.e., joint
selection of a subset of the assets that compose the index and computation
of their relative weights (capital allocation). The level of sparsity of
the portfolios, i.e., the number of selected assets, is controlled through
a regularization parameter. Different tracking measures are available,
namely, the empirical tracking error (ETE), downside risk (DR), Huber
empirical tracking error (HETE), and Huber downside risk (HDR). See
vignette for a detailed documentation and comparison, with several
illustrative examples. The package is based on the paper: K. Benidis, Y.
Feng, and D. P. Palomar, "Sparse Portfolios for High-Dimensional Financial
Index Tracking," IEEE Trans. on Signal Processing, vol. 66, no. 1, pp.
155-170, Jan. 2018. <doi:10.1109/TSP.2017.2762286>.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
