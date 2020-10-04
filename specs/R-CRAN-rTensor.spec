%global packname  rTensor
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tools for Tensor Analysis and Decomposition

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-methods 
Requires:         R-methods 

%description
A set of tools for creation, manipulation, and modeling of tensors with
arbitrary number of modes. A tensor in the context of data analysis is a
multidimensional array. rTensor does this by providing a S4 class 'Tensor'
that wraps around the base 'array' class. rTensor provides common tensor
operations as methods, including matrix unfolding, summing/averaging
across modes, calculating the Frobenius norm, and taking the inner product
between two tensors. Familiar array operations are overloaded, such as
index subsetting via '[' and element-wise operations. rTensor also
implements various tensor decomposition, including CP, GLRAM, MPCA, PVD,
and Tucker. For tensors with 3 modes, rTensor also implements transpose,
t-product, and t-SVD, as defined in Kilmer et al. (2013). Some auxiliary
functions include the Khatri-Rao product, Kronecker product, and the
Hamadard product for a list of matrices.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
