%global __brp_check_rpaths %{nil}
%global packname  flamingos
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Functional Latent Data Models for Clustering HeterogeneousCurves ('FLaMingos')

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Provides a variety of original and flexible user-friendly statistical
latent variable models for the simultaneous clustering and segmentation of
heterogeneous functional data (i.e time series, or more generally
longitudinal data, fitted by unsupervised algorithms, including EM
algorithms. Functional Latent Data Models for Clustering heterogeneous
curves ('FLaMingos') are originally introduced and written in 'Matlab' by
Faicel Chamroukhi
<https://github.com/fchamroukhi?utf8=?&tab=repositories&q=mix&type=public&language=matlab>.
The references are mainly the following ones. Chamroukhi F. (2010)
<https://chamroukhi.com/FChamroukhi-PhD.pdf>. Chamroukhi F., Same A.,
Govaert, G. and Aknin P. (2010) <doi:10.1016/j.neucom.2009.12.023>.
Chamroukhi F., Same A., Aknin P. and Govaert G. (2011).
<doi:10.1109/IJCNN.2011.6033590>. Same A., Chamroukhi F., Govaert G. and
Aknin, P. (2011) <doi:10.1007/s11634-011-0096-5>. Chamroukhi F., and
Glotin H. (2012) <doi:10.1109/IJCNN.2012.6252818>. Chamroukhi F., Glotin
H. and Same A. (2013) <doi:10.1016/j.neucom.2012.10.030>. Chamroukhi F.
(2015) <https://chamroukhi.com/FChamroukhi-HDR.pdf>. Chamroukhi F. and
Nguyen H-D. (2019) <doi:10.1002/widm.1298>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
