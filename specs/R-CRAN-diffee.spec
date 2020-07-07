%global packname  diffee
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Fast and Scalable Learning of Sparse Changes in High-DimensionalGaussian Graphical Model Structure

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-pcaPP 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-pcaPP 

%description
This is an R implementation of Fast and Scalable Learning of Sparse
Changes in High-Dimensional Gaussian Graphical Model Structure (DIFFEE).
The DIFFEE algorithm can be used to fast estimate the differential network
between two related datasets. For instance, it can identify differential
gene network from datasets of case and control. By performing data-driven
network inference from two high-dimensional data sets, this tool can help
users effectively translate two aggregated data blocks into knowledge of
the changes among entities between two Gaussian Graphical Model. Please
run demo(diffeeDemo) to learn the basic functions provided by this
package. For further details, please read the original paper: Beilun Wang,
Arshdeep Sekhon, Yanjun Qi (2018) <arXiv:1710.11223>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
