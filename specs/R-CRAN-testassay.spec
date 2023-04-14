%global __brp_check_rpaths %{nil}
%global packname  testassay
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Hypothesis Testing Framework for Validating an Assay forPrecision

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
A common way of validating a biological assay for is through a procedure,
where m levels of an analyte are measured with n replicates at each level,
and if all m estimates of the coefficient of variation (CV) are less than
some prespecified level, then the assay is declared validated for
precision within the range of the m analyte levels. Two limitations of
this procedure are: there is no clear statistical statement of precision
upon passing, and it is unclear how to modify the procedure for assays
with constant standard deviation. We provide tools to convert such a
procedure into a set of m hypothesis tests. This reframing motivates the
m:n:q procedure, which upon completion delivers a 100q% upper confidence
limit on the CV. Additionally, for a post-validation assay output of y,
the method gives an ``effective standard deviation interval'' of log(y)
plus or minus r, which is a 68% confidence interval on log(mu), where mu
is the expected value of the assay output for that sample. Further, the
m:n:q procedure can be straightforwardly applied to constant standard
deviation assays. We illustrate these tools by applying them to a growth
inhibition assay. This is an implementation of the methods described in
Fay, Sachs, and Miura (2018) <doi:10.1002/sim.7528>.

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
%{rlibdir}/%{packname}
